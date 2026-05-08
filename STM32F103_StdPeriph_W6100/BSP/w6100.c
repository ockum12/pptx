/**
 * @file    w6100.c
 * @brief   W6100 SPI access stub for STM32F103 (StdPeriph)
 *
 * ─────────────────────────────────────────────────────────────────────
 * Integration note – full W6100 / ioLibrary driver
 * ─────────────────────────────────────────────────────────────────────
 * This file provides a minimal SPI frame implementation so the project
 * compiles and the VERSIONR demo in main.c works.
 *
 * To use the full WIZnet ioLibrary_Driver:
 *   1. Clone https://github.com/Wiznet/ioLibrary_Driver.git
 *      into Drivers/ioLibrary_Driver/
 *   2. Add the following to your include paths:
 *        Drivers/ioLibrary_Driver/Ethernet
 *        Drivers/ioLibrary_Driver/Ethernet/W6100
 *        Drivers/ioLibrary_Driver/Internet  (optional)
 *   3. In wizchip_conf.c / w6100.c implement the SPI callbacks using
 *      SPI1_TransferByte() from spi.c:
 *
 *        void  wizchip_select(void)   { W6100_CS_LOW();  }
 *        void  wizchip_deselect(void) { W6100_CS_HIGH(); }
 *        uint8_t wizchip_read(void)
 *            { return SPI1_TransferByte(0x00); }
 *        void wizchip_write(uint8_t wb)
 *            { SPI1_TransferByte(wb); }
 *
 *   4. Call reg_wizchip_cs_cbfunc() / reg_wizchip_spi_cbfunc() with
 *      the above callbacks, then wizchip_init() / wizchip_setnetinfo().
 * ─────────────────────────────────────────────────────────────────────
 *
 * SPI frame for W6100 common-block access
 * ┌──────────┬──────────┬─────────┬──────────────────┐
 * │ Addr[15:8]│ Addr[7:0]│ Control │ Data[0..N-1]     │
 * └──────────┴──────────┴─────────┴──────────────────┘
 */

#include "w6100.h"
#include "spi.h"

/* ═══════════════════════════════════════════════════════════════════════
 *  Internal helper – send address + control, keep CS asserted
 * ═══════════════════════════════════════════════════════════════════════ */
static void W6100_StartFrame(uint16_t addr, uint8_t ctrl)
{
    W6100_CS_LOW();
    SPI1_TransferByte((uint8_t)(addr >> 8));    /* high address byte    */
    SPI1_TransferByte((uint8_t)(addr & 0xFF));  /* low  address byte    */
    SPI1_TransferByte(ctrl);                    /* control byte         */
}

/* ═══════════════════════════════════════════════════════════════════════
 *  W6100_Init
 * ═══════════════════════════════════════════════════════════════════════ */
void W6100_Init(void)
{
    /*
     * Software reset: write 0x80 to MR, then wait for it to self-clear.
     *
     * If you have a dedicated RESET pin connected to the W6100:
     *   1. Add a GPIO output definition for RESET_PIN in spi.h
     *   2. Assert RESET low for ≥ 500 µs, then high
     *   3. Wait ≥ 150 ms before the first SPI transaction
     *   Replace the software-reset block below with the hardware sequence.
     */
    W6100_WriteReg8(W6100_REG_MR, 0x80);

    /* Wait for the reset bit to clear */
    {
        volatile uint32_t timeout = 100000UL;
        while ((W6100_ReadReg8(W6100_REG_MR) & 0x80) && timeout--)
        {
            /* wait */
        }
    }
}

/* ═══════════════════════════════════════════════════════════════════════
 *  W6100_ReadReg8
 * ═══════════════════════════════════════════════════════════════════════ */
uint8_t W6100_ReadReg8(uint16_t addr)
{
    uint8_t val;
    W6100_StartFrame(addr, W6100_CTRL_COMMON_READ);
    val = SPI1_TransferByte(0x00);              /* dummy TX, capture RX */
    W6100_CS_HIGH();
    return val;
}

/* ═══════════════════════════════════════════════════════════════════════
 *  W6100_WriteReg8
 * ═══════════════════════════════════════════════════════════════════════ */
void W6100_WriteReg8(uint16_t addr, uint8_t data)
{
    W6100_StartFrame(addr, W6100_CTRL_COMMON_WRITE);
    SPI1_TransferByte(data);
    W6100_CS_HIGH();
}

/* ═══════════════════════════════════════════════════════════════════════
 *  W6100_ReadBuf
 * ═══════════════════════════════════════════════════════════════════════ */
void W6100_ReadBuf(uint16_t addr, uint8_t *buf, uint16_t len)
{
    uint16_t i;
    W6100_StartFrame(addr, W6100_CTRL_COMMON_READ);
    for (i = 0; i < len; i++)
    {
        buf[i] = SPI1_TransferByte(0x00);
    }
    W6100_CS_HIGH();
}

/* ═══════════════════════════════════════════════════════════════════════
 *  W6100_WriteBuf
 * ═══════════════════════════════════════════════════════════════════════ */
void W6100_WriteBuf(uint16_t addr, const uint8_t *buf, uint16_t len)
{
    uint16_t i;
    W6100_StartFrame(addr, W6100_CTRL_COMMON_WRITE);
    for (i = 0; i < len; i++)
    {
        SPI1_TransferByte(buf[i]);
    }
    W6100_CS_HIGH();
}

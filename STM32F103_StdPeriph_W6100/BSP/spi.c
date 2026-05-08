/**
 * @file    spi.c
 * @brief   SPI1 BSP implementation using the STM32F10x StdPeriph library.
 *
 * Uses StdPeriph functions (SPI_Init, SPI_I2S_SendData, etc.) – NOT HAL.
 *
 * If you need to change the SPI baud rate, edit the BaudRatePrescaler
 * field in SPI1_Init().  At 72 MHz PCLK2:
 *   SPI_BaudRatePrescaler_2   → ~36 MHz
 *   SPI_BaudRatePrescaler_4   → ~18 MHz
 *   SPI_BaudRatePrescaler_8   → ~ 9 MHz  ← default
 *   SPI_BaudRatePrescaler_16  → ~4.5 MHz
 */

#include "spi.h"
#include "stm32f10x_rcc.h"
#include "stm32f10x_gpio.h"
#include "stm32f10x_spi.h"

/* ═══════════════════════════════════════════════════════════════════════
 *  SPI1_Init
 * ═══════════════════════════════════════════════════════════════════════ */
void SPI1_Init(void)
{
    GPIO_InitTypeDef  gpio;
    SPI_InitTypeDef   spi;

    /* ── 1. Enable clocks ─────────────────────────────────────────── */
    RCC_APB2PeriphClockCmd(SPI1_GPIO_RCC | RCC_APB2Periph_SPI1, ENABLE);
    /* CS pin is on GPIOA – clock already enabled above.               */
    /* If CS is on a different port, add its RCC_APB2Periph_GPIOx here. */

    /* ── 2. SPI1 pins (SCK, MOSI = AF push-pull; MISO = input float) */
    gpio.GPIO_Pin   = SPI1_SCK_PIN | SPI1_MOSI_PIN;
    gpio.GPIO_Mode  = GPIO_Mode_AF_PP;
    gpio.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(SPI1_GPIO_PORT, &gpio);

    gpio.GPIO_Pin   = SPI1_MISO_PIN;
    gpio.GPIO_Mode  = GPIO_Mode_IN_FLOATING;
    GPIO_Init(SPI1_GPIO_PORT, &gpio);

    /* ── 3. CS pin (push-pull output, default HIGH / deasserted) ──── */
    gpio.GPIO_Pin   = W6100_CS_PIN;
    gpio.GPIO_Mode  = GPIO_Mode_Out_PP;
    gpio.GPIO_Speed = GPIO_Speed_50MHz;
    GPIO_Init(W6100_CS_GPIO_PORT, &gpio);
    W6100_CS_HIGH();

    /* ── 4. SPI1 peripheral ───────────────────────────────────────── */
    SPI_I2S_DeInit(SPI1);

    spi.SPI_Mode              = SPI_Mode_Master;
    spi.SPI_Direction         = SPI_Direction_2Lines_FullDuplex;
    spi.SPI_DataSize          = SPI_DataSize_8b;
    spi.SPI_CPOL              = SPI_CPOL_Low;   /* W6100: Mode 0 or 3  */
    spi.SPI_CPHA              = SPI_CPHA_1Edge;
    spi.SPI_NSS               = SPI_NSS_Soft;
    spi.SPI_BaudRatePrescaler = SPI_BaudRatePrescaler_8; /* ~9 MHz     */
    spi.SPI_FirstBit          = SPI_FirstBit_MSB;
    spi.SPI_CRCPolynomial     = 7;
    SPI_Init(SPI1, &spi);

    SPI_Cmd(SPI1, ENABLE);
}

/* ═══════════════════════════════════════════════════════════════════════
 *  SPI1_TransferByte
 * ═══════════════════════════════════════════════════════════════════════ */
uint8_t SPI1_TransferByte(uint8_t tx)
{
    /* Wait until TX buffer is empty */
    while (SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_TXE) == RESET)
    {
        /* wait */
    }
    SPI_I2S_SendData(SPI1, tx);

    /* Wait until a byte is received */
    while (SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_RXNE) == RESET)
    {
        /* wait */
    }

    /* Wait until bus is not busy */
    while (SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_BSY) == SET)
    {
        /* wait */
    }

    return (uint8_t)SPI_I2S_ReceiveData(SPI1);
}

/* ═══════════════════════════════════════════════════════════════════════
 *  SPI1_Transfer
 * ═══════════════════════════════════════════════════════════════════════ */
void SPI1_Transfer(const uint8_t *tx, uint8_t *rx, uint16_t len)
{
    uint16_t i;

    for (i = 0; i < len; i++)
    {
        while (SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_TXE) == RESET)
        {
            /* wait */
        }
        SPI_I2S_SendData(SPI1, tx[i]);

        while (SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_RXNE) == RESET)
        {
            /* wait */
        }
        rx[i] = (uint8_t)SPI_I2S_ReceiveData(SPI1);
    }

    /* Wait until the last byte is fully shifted out */
    while (SPI_I2S_GetFlagStatus(SPI1, SPI_I2S_FLAG_BSY) == SET)
    {
        /* wait */
    }
}

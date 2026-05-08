/**
 * @file    w6100.h
 * @brief   W6100 SPI BSP – register addresses and public API
 *
 * The W6100 is accessed over SPI using a 3-phase frame:
 *   [Address (2 bytes)] [Control (1 byte)] [Data (N bytes)]
 *
 * Control byte format:
 *   Bit 7-5 : Block select   (000 = Common, 001-100 = Socket 0-3, …)
 *   Bit   4 : Reserved (0)
 *   Bit 3-2 : BSB            (Block Select Bit, combined with above)
 *   Bit   1 : RWB            (0 = Read, 1 = Write)
 *   Bit   0 : OM             (0 = VDM, 1 = FDM1)
 *
 * This stub implements only direct common-register read/write.
 * Replace / extend with a full W6100 driver (e.g. ioLibrary_Driver)
 * as described in the integration notes in w6100.c.
 */

#ifndef __W6100_H
#define __W6100_H

#ifdef __cplusplus
extern "C" {
#endif

#include "stm32f10x.h"

/* ── W6100 Common Register addresses (partial list) ─────────────────── */
#define W6100_REG_MR         0x0000U  /* Mode Register                 */
#define W6100_REG_GAR        0x0001U  /* Gateway Address (4 bytes)     */
#define W6100_REG_SUBR       0x0005U  /* Subnet Mask     (4 bytes)     */
#define W6100_REG_SHAR       0x0009U  /* MAC Address     (6 bytes)     */
#define W6100_REG_SIPR       0x000FU  /* Source IP       (4 bytes)     */
#define W6100_REG_INTLEVEL   0x0013U  /* Interrupt Level Timer         */
#define W6100_REG_IR         0x0015U  /* Interrupt Register            */
#define W6100_REG_IMR        0x0016U  /* Interrupt Mask                */
#define W6100_REG_SIR        0x0017U  /* Socket Interrupt              */
#define W6100_REG_SIMR       0x0018U  /* Socket Interrupt Mask         */
#define W6100_REG_RTR        0x0019U  /* Retry Time                    */
#define W6100_REG_RCR        0x001BU  /* Retry Count                   */
#define W6100_REG_PTIMER     0x001CU  /* PPP Link Control Timer        */
#define W6100_REG_PMAGIC     0x001DU  /* PPP LCP Magic Number          */
#define W6100_REG_PHAR       0x001EU  /* PPP Dest MAC Address          */
#define W6100_REG_PSID       0x0024U  /* PPP Session ID                */
#define W6100_REG_PMRU       0x0026U  /* PPP Max Segment Size          */
#define W6100_REG_UIPR       0x0028U  /* Unreachable IP                */
#define W6100_REG_UPORTR     0x002CU  /* Unreachable Port              */
#define W6100_REG_PHYCFGR    0x002EU  /* PHY Configuration             */
#define W6100_REG_VERSIONR   0x0039U  /* Chip version (read: 0x04)     */

/* ── Control byte helpers ────────────────────────────────────────────── */
#define W6100_CTRL_COMMON_READ  0x00U  /* BSB=000, RWB=0, OM=0 (VDM)  */
#define W6100_CTRL_COMMON_WRITE 0x04U  /* BSB=000, RWB=1, OM=0 (VDM)  */

/* ── Public API ──────────────────────────────────────────────────────── */

/**
 * @brief  Hardware reset and basic initialisation of W6100.
 *         Asserts /CS high, drives RESET low then high.
 *         If no dedicated RESET pin is used, it performs a software
 *         reset via the MR register instead.
 */
void W6100_Init(void);

/**
 * @brief  Read one byte from a W6100 common register.
 * @param  addr  16-bit register address.
 * @return Register value.
 */
uint8_t W6100_ReadReg8(uint16_t addr);

/**
 * @brief  Write one byte to a W6100 common register.
 * @param  addr  16-bit register address.
 * @param  data  Value to write.
 */
void W6100_WriteReg8(uint16_t addr, uint8_t data);

/**
 * @brief  Read multiple bytes starting at addr (common block).
 * @param  addr  Start address.
 * @param  buf   Destination buffer.
 * @param  len   Number of bytes.
 */
void W6100_ReadBuf(uint16_t addr, uint8_t *buf, uint16_t len);

/**
 * @brief  Write multiple bytes starting at addr (common block).
 * @param  addr  Start address.
 * @param  buf   Source buffer.
 * @param  len   Number of bytes.
 */
void W6100_WriteBuf(uint16_t addr, const uint8_t *buf, uint16_t len);

#ifdef __cplusplus
}
#endif

#endif /* __W6100_H */

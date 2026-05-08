/**
 * @file    spi.h
 * @brief   SPI1 BSP – StdPeriph-based SPI init and transfer
 *
 * Hardware mapping (STM32F103C8T6 / Blue Pill):
 *   PA5  – SPI1_SCK
 *   PA6  – SPI1_MISO
 *   PA7  – SPI1_MOSI
 *   PA4  – W6100 /CS  (GPIO, software-controlled)
 */

#ifndef __SPI_H
#define __SPI_H

#ifdef __cplusplus
extern "C" {
#endif

#include "stm32f10x.h"

/* ── Pin definitions ─────────────────────────────────────────────────── */
#define SPI1_GPIO_PORT      GPIOA
#define SPI1_SCK_PIN        GPIO_Pin_5
#define SPI1_MISO_PIN       GPIO_Pin_6
#define SPI1_MOSI_PIN       GPIO_Pin_7
#define SPI1_GPIO_RCC       RCC_APB2Periph_GPIOA

/* W6100 Chip-Select – change port/pin to match your schematic           */
#define W6100_CS_GPIO_PORT  GPIOA
#define W6100_CS_PIN        GPIO_Pin_4
#define W6100_CS_RCC        RCC_APB2Periph_GPIOA

/* ── CS macros ───────────────────────────────────────────────────────── */
#define W6100_CS_LOW()   GPIO_ResetBits(W6100_CS_GPIO_PORT, W6100_CS_PIN)
#define W6100_CS_HIGH()  GPIO_SetBits(W6100_CS_GPIO_PORT,   W6100_CS_PIN)

/* ── Public API ──────────────────────────────────────────────────────── */

/**
 * @brief Initialise SPI1 and the W6100 CS GPIO.
 *
 * Call once, before any SPI transfer.
 * Settings: Master, 8-bit, CPOL=0/CPHA=0 (Mode 0), MSB first,
 *           Software NSS, PCLK2/8 (≈ 9 MHz at 72 MHz SYSCLK).
 */
void SPI1_Init(void);

/**
 * @brief  Send one byte and receive one byte simultaneously.
 * @param  tx  Byte to transmit.
 * @return Received byte.
 */
uint8_t SPI1_TransferByte(uint8_t tx);

/**
 * @brief  Transfer a buffer of bytes (full-duplex).
 * @param  tx   Pointer to transmit buffer (must not be NULL).
 * @param  rx   Pointer to receive buffer  (may be same as tx).
 * @param  len  Number of bytes.
 */
void SPI1_Transfer(const uint8_t *tx, uint8_t *rx, uint16_t len);

#ifdef __cplusplus
}
#endif

#endif /* __SPI_H */

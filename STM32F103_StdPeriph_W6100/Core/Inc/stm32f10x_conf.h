/**
 * @file    stm32f10x_conf.h
 * @brief   StdPeriph library configuration file
 *
 * Enable only the peripheral modules your application uses.
 * Uncomment additional includes as needed.
 */

#ifndef __STM32F10x_CONF_H
#define __STM32F10x_CONF_H

/* ── Peripheral module enables ───────────────────────────────────────── */
/* ADC */
/* #include "stm32f10x_adc.h" */

/* BKP */
/* #include "stm32f10x_bkp.h" */

/* CAN */
/* #include "stm32f10x_can.h" */

/* CRC */
/* #include "stm32f10x_crc.h" */

/* DAC */
/* #include "stm32f10x_dac.h" */

/* DBGMCU */
/* #include "stm32f10x_dbgmcu.h" */

/* DMA */
/* #include "stm32f10x_dma.h" */

/* EXTI */
/* #include "stm32f10x_exti.h" */

/* FLASH */
/* #include "stm32f10x_flash.h" */

/* FSMC */
/* #include "stm32f10x_fsmc.h" */

/* GPIO  ← required */
#include "stm32f10x_gpio.h"

/* I2C */
/* #include "stm32f10x_i2c.h" */

/* IWDG */
/* #include "stm32f10x_iwdg.h" */

/* PWR */
/* #include "stm32f10x_pwr.h" */

/* RCC  ← required */
#include "stm32f10x_rcc.h"

/* RTC */
/* #include "stm32f10x_rtc.h" */

/* SDIO */
/* #include "stm32f10x_sdio.h" */

/* SPI  ← required */
#include "stm32f10x_spi.h"

/* TIM */
/* #include "stm32f10x_tim.h" */

/* USART */
/* #include "stm32f10x_usart.h" */

/* WWDG */
/* #include "stm32f10x_wwdg.h" */

/* Misc (NVIC / SysTick helper) */
#include "misc.h"

/* ── Runtime checks (define to enable assert_param) ─────────────────── */
#ifdef  USE_FULL_ASSERT
#define assert_param(expr) \
    ((expr) ? (void)0 : assert_failed((uint8_t *)__FILE__, __LINE__))
void assert_failed(uint8_t *file, uint32_t line);
#else
#define assert_param(expr) ((void)0)
#endif /* USE_FULL_ASSERT */

#endif /* __STM32F10x_CONF_H */

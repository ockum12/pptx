/**
 * @file    main.h
 * @brief   STM32F103 StdPeriph + W6100 SPI project – main header
 *
 * Target:  STM32F103C8T6 (Blue Pill / medium-density)
 * Library: STM32F10x Standard Peripheral Library (StdPeriph)
 */

#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* ── StdPeriph base header ───────────────────────────────────────────── */
#include "stm32f10x.h"

/* ── Board-Support headers ───────────────────────────────────────────── */
#include "spi.h"
#include "w6100.h"

/* ── On-board LED (PC13 on Blue Pill, active-low) ────────────────────── */
#define LED_GPIO_PORT   GPIOC
#define LED_GPIO_PIN    GPIO_Pin_13
#define LED_RCC_PERIPH  RCC_APB2Periph_GPIOC

static inline void LED_On(void)  { GPIO_ResetBits(LED_GPIO_PORT, LED_GPIO_PIN); }
static inline void LED_Off(void) { GPIO_SetBits(LED_GPIO_PORT, LED_GPIO_PIN);   }
static inline void LED_Toggle(void)
{
    if (GPIO_ReadOutputDataBit(LED_GPIO_PORT, LED_GPIO_PIN))
        GPIO_ResetBits(LED_GPIO_PORT, LED_GPIO_PIN);
    else
        GPIO_SetBits(LED_GPIO_PORT, LED_GPIO_PIN);
}

/* ── Prototype ───────────────────────────────────────────────────────── */
/* (SystemInit is declared in system_stm32f10x.h via CMSIS)             */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */

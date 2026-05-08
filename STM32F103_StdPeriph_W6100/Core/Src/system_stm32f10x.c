/**
 * @file    system_stm32f10x.c
 * @brief   STM32F10x system clock configuration
 *
 * Configures:
 *   HSE  = 8 MHz  (typical Blue Pill / Nucleo crystal)
 *   PLL  × 9 → SYSCLK = 72 MHz
 *   AHB  / 1 → HCLK   = 72 MHz
 *   APB1 / 2 → PCLK1  = 36 MHz  (≤ 36 MHz limit)
 *   APB2 / 1 → PCLK2  = 72 MHz
 *   Flash latency: 2 wait states (required above 48 MHz)
 *
 * This file replaces the CubeMX-generated system_stm32f10x.c when
 * using the StdPeriph library directly.
 */

#include "stm32f10x.h"

/* Exported variable read by StdPeriph / CMSIS ───────────────────────── */
uint32_t SystemCoreClock = 72000000UL;

/* ═══════════════════════════════════════════════════════════════════════
 *  SystemInit
 *  Called automatically from the startup file before main().
 * ═══════════════════════════════════════════════════════════════════════ */
void SystemInit(void)
{
    /* ── 1. Enable HSE and wait for it to be ready ─────────────────── */
    RCC->CR |= RCC_CR_HSEON;
    while (!(RCC->CR & RCC_CR_HSERDY))
    {
        /* wait */
    }

    /* ── 2. Flash prefetch + 2 wait states ─────────────────────────── */
    FLASH->ACR = FLASH_ACR_PRFTBE | FLASH_ACR_LATENCY_2;

    /* ── 3. AHB / APB prescalers ────────────────────────────────────── */
    /* HCLK  = SYSCLK / 1                                               */
    RCC->CFGR |= RCC_CFGR_HPRE_DIV1;
    /* PCLK2 = HCLK   / 1                                               */
    RCC->CFGR |= RCC_CFGR_PPRE2_DIV1;
    /* PCLK1 = HCLK   / 2                                               */
    RCC->CFGR |= RCC_CFGR_PPRE1_DIV2;

    /* ── 4. PLL: HSE × 9 = 72 MHz ──────────────────────────────────── */
    RCC->CFGR |= RCC_CFGR_PLLSRC       /* PLL source = HSE             */
              |  RCC_CFGR_PLLMULL9;    /* PLL × 9                      */

    /* ── 5. Enable PLL and wait ─────────────────────────────────────── */
    RCC->CR |= RCC_CR_PLLON;
    while (!(RCC->CR & RCC_CR_PLLRDY))
    {
        /* wait */
    }

    /* ── 6. Switch SYSCLK to PLL ────────────────────────────────────── */
    RCC->CFGR &= ~RCC_CFGR_SW;
    RCC->CFGR |=  RCC_CFGR_SW_PLL;
    while ((RCC->CFGR & RCC_CFGR_SWS) != RCC_CFGR_SWS_PLL)
    {
        /* wait */
    }

    /* SystemCoreClock already set at compile time (72 MHz) */
}

/* ═══════════════════════════════════════════════════════════════════════
 *  SystemCoreClockUpdate  (required by CMSIS)
 * ═══════════════════════════════════════════════════════════════════════ */
void SystemCoreClockUpdate(void)
{
    SystemCoreClock = 72000000UL;
}

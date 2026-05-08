/**
 * @file    main.c
 * @brief   STM32F103C8T6 – StdPeriph + W6100 SPI template
 *
 * ─────────────────────────────────────────────────────────────────────
 * Build in STM32CubeIDE
 * ─────────────────────────────────────────────────────────────────────
 *  1. Open STM32CubeIDE → File → Open Projects from File System
 *     and select this folder, OR import as a Makefile/C project.
 *
 *  2. Add Include paths (Project → Properties → C/C++ Build →
 *     Settings → MCU GCC Compiler → Includes):
 *       • ../Core/Inc
 *       • ../BSP
 *       • ../Drivers/StdPeriph/inc
 *       • ../Drivers/CMSIS/CM3/CoreSupport
 *       • ../Drivers/CMSIS/CM3/DeviceSupport/ST/STM32F10x
 *
 *  3. Add Preprocessor Symbols (same dialog, tab "Preprocessor"):
 *       • USE_STDPERIPH_DRIVER
 *       • STM32F10X_MD
 *
 *  4. Copy the StdPeriph driver sources into Drivers/StdPeriph/
 *     (see Drivers/StdPeriph/README.md for where to get them).
 *
 *  5. Build (Ctrl+B).
 * ─────────────────────────────────────────────────────────────────────
 *
 * Pin mapping (SPI1 on Blue Pill):
 *   PA5  – SPI1_SCK
 *   PA6  – SPI1_MISO
 *   PA7  – SPI1_MOSI
 *   PA4  – W6100 /CS  (software-controlled GPIO)
 *   PC13 – On-board LED (active-low)
 */

#include "main.h"

/* ── Private function prototypes ─────────────────────────────────────── */
static void LED_GPIO_Init(void);
static void Delay_ms(volatile uint32_t ms);

/* ── SysTick tick counter ────────────────────────────────────────────── */
static volatile uint32_t g_tick = 0;

/* ═══════════════════════════════════════════════════════════════════════
 *  main
 * ═══════════════════════════════════════════════════════════════════════ */
int main(void)
{
    /* 1. System clock (72 MHz via PLL, defined in system_stm32f10x.c)    */
    SystemInit();

    /* 2. SysTick at 1 ms for simple delay                                */
    SysTick_Config(SystemCoreClock / 1000);

    /* 3. On-board LED                                                    */
    LED_GPIO_Init();
    LED_Off();

    /* 4. SPI1 peripheral + W6100 CS pin                                  */
    SPI1_Init();

    /* 5. W6100 hardware reset + basic register check                     */
    W6100_Init();

    /* 6. Demo: read W6100 VERSIONR (register 0x0039, expected 0x04)      */
    {
        uint8_t ver = W6100_ReadReg8(W6100_REG_VERSIONR);
        if (ver == 0x04)
        {
            /* W6100 detected – blink fast to signal OK                   */
            LED_On();
        }
        else
        {
            /* Unexpected value – blink slow to signal error              */
            LED_Off();
        }
    }

    /* ── Main loop ────────────────────────────────────────────────────── */
    while (1)
    {
        LED_Toggle();
        Delay_ms(500);

        /*
         * ── W6100 integration point ──────────────────────────────────
         * Place your W6100 driver calls here, for example:
         *
         *   W6100_WriteReg8(W6100_REG_MR, 0x80);   // software reset
         *   Delay_ms(10);
         *   W6100_ConfigNetwork(&netInfo);
         *   while (1) { wizchip_run(); }
         * ─────────────────────────────────────────────────────────────
         */
    }
}

/* ── SysTick handler ─────────────────────────────────────────────────── */
void SysTick_Handler(void)
{
    g_tick++;
}

/* ── Simple millisecond delay ────────────────────────────────────────── */
static void Delay_ms(volatile uint32_t ms)
{
    uint32_t start = g_tick;
    while ((g_tick - start) < ms)
    {
        __NOP();
    }
}

/* ── LED GPIO initialisation (PC13, active-low) ──────────────────────── */
static void LED_GPIO_Init(void)
{
    GPIO_InitTypeDef gpio;

    RCC_APB2PeriphClockCmd(LED_RCC_PERIPH, ENABLE);

    gpio.GPIO_Pin   = LED_GPIO_PIN;
    gpio.GPIO_Mode  = GPIO_Mode_Out_PP;
    gpio.GPIO_Speed = GPIO_Speed_2MHz;
    GPIO_Init(LED_GPIO_PORT, &gpio);
}

# Drivers/StdPeriph

## 개요 (Overview)

이 폴더는 **STM32F10x Standard Peripheral Library (StdPeriph)** 소스 파일을 담는 곳입니다.  
STM32CubeIDE 기본 패키지에는 포함되지 않으므로 **직접 구해서** 아래 위치에 복사해야 합니다.

This folder holds the **STM32F10x Standard Peripheral Library (StdPeriph)** sources.  
They are not bundled with STM32CubeIDE; you must obtain them separately and copy them here.

---

## 필요한 폴더 구조 (Required folder structure)

```text
Drivers/StdPeriph/
├── inc/                       ← header files (.h)
│   ├── misc.h
│   ├── stm32f10x_gpio.h
│   ├── stm32f10x_rcc.h
│   ├── stm32f10x_spi.h
│   └── (others as needed)
└── src/                       ← source files (.c)
    ├── misc.c
    ├── stm32f10x_gpio.c
    ├── stm32f10x_rcc.c
    ├── stm32f10x_spi.c
    └── (others as needed)
```

---

## 소스 구하는 방법 (How to obtain the sources)

### 방법 1 – GitHub (unofficial mirror)
ST 공식 배포물의 미러를 GitHub에서 찾을 수 있습니다:

```
Search: "STM32F10x_StdPeriph_Lib" on GitHub
```

다운로드 후 압축 해제하면 아래 경로에 파일이 있습니다:
```
STM32F10x_StdPeriph_Lib_Vx.x.x/Libraries/STM32F10x_StdPeriph_Driver/
```
`inc/` 와 `src/` 를 이 폴더 안에 복사하세요.

### 방법 2 – STMicroelectronics 공식 사이트
- <https://www.st.com> 에서 `STM32F10x Standard Peripheral Library` 검색
- ZIP 다운로드 후 위와 동일하게 복사

---

## 최소 필요 파일 (Minimum files for SPI + GPIO)

| 파일 | 역할 |
|------|------|
| `stm32f10x_rcc.c/.h`  | Clock enable         |
| `stm32f10x_gpio.c/.h` | GPIO init            |
| `stm32f10x_spi.c/.h`  | SPI init & transfer  |
| `misc.c/.h`           | NVIC / SysTick helper |

---

## CMSIS 파일 위치

CMSIS 관련 파일(`core_cm3.h`, `stm32f10x.h`, `system_stm32f10x.h`)은  
`Drivers/CMSIS/` 폴더의 README를 참조하세요.

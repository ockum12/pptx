# STM32F103_StdPeriph_W6100

**STM32F103C8T6** 용 **STM32CubeIDE** 프로젝트 템플릿  
Standard Peripheral Library (StdPeriph) 기반 · SPI/W6100 연동 예제

---

## 프로젝트 개요

| 항목 | 내용 |
|------|------|
| 타깃 MCU | STM32F103C8T6 (Blue Pill 등) |
| 라이브러리 | STM32F10x Standard Peripheral Library |
| IDE | STM32CubeIDE 1.x |
| SPI 포트 | SPI1 (PA5=SCK, PA6=MISO, PA7=MOSI, PA4=W6100 CS) |
| LED | PC13 (Active-Low) |
| 클럭 | HSE 8 MHz → PLL ×9 = 72 MHz |

---

## 폴더 구조

```text
STM32F103_StdPeriph_W6100/
├── .cproject                      ← STM32CubeIDE C 빌드 설정
├── .project                       ← Eclipse 프로젝트 메타데이터
├── STM32F103C8TX_FLASH.ld         ← 링커 스크립트
├── Core/
│   ├── Inc/
│   │   ├── main.h                 ← LED/핀 정의 및 헤더 포함
│   │   └── stm32f10x_conf.h       ← StdPeriph 모듈 선택 헤더
│   └── Src/
│       ├── main.c                 ← 애플리케이션 진입점 + W6100 데모
│       └── system_stm32f10x.c    ← 시스템 클럭 초기화 (72 MHz)
├── BSP/
│   ├── spi.c / spi.h              ← SPI1 초기화 및 전송 (StdPeriph)
│   └── w6100.c / w6100.h         ← W6100 SPI 프레임 read/write stub
├── Drivers/
│   ├── StdPeriph/
│   │   ├── README.md              ← ← StdPeriph 소스 복사 안내
│   │   ├── inc/                   ← StdPeriph 헤더 (직접 복사)
│   │   └── src/                   ← StdPeriph 소스 (직접 복사)
│   └── CMSIS/
│       ├── README.md              ← CMSIS 파일 복사 안내
│       └── CM3/                   ← CMSIS 파일 (직접 복사)
└── startup/
    └── startup_stm32f103c8tx.s    ← Cortex-M3 스타트업 어셈블리
```

---

## 빌드 전 준비 (필수)

### 1. StdPeriph 라이브러리 소스 복사

StdPeriph 소스는 이 저장소에 포함되지 않습니다. 별도로 구해서 복사하세요.

**소스 위치** (STM32F10x_StdPeriph_Lib 압축 해제 후):
```
Libraries/STM32F10x_StdPeriph_Driver/inc/  → Drivers/StdPeriph/inc/
Libraries/STM32F10x_StdPeriph_Driver/src/  → Drivers/StdPeriph/src/
Libraries/CMSIS/CM3/CoreSupport/           → Drivers/CMSIS/CM3/CoreSupport/
Libraries/CMSIS/CM3/DeviceSupport/ST/      → Drivers/CMSIS/CM3/DeviceSupport/ST/
```

최소 필요 파일 (SPI + GPIO 기준):

| 경로 | 파일 |
|------|------|
| `Drivers/StdPeriph/src/` | `stm32f10x_rcc.c`, `stm32f10x_gpio.c`, `stm32f10x_spi.c`, `misc.c` |
| `Drivers/StdPeriph/inc/` | `stm32f10x_rcc.h`, `stm32f10x_gpio.h`, `stm32f10x_spi.h`, `misc.h` |
| `Drivers/CMSIS/CM3/CoreSupport/` | `core_cm3.h`, `core_cm3.c` |
| `Drivers/CMSIS/CM3/DeviceSupport/ST/STM32F10x/` | `stm32f10x.h`, `system_stm32f10x.h` |

---

## STM32CubeIDE에서 빌드하는 방법

### 방법 A – 프로젝트 가져오기 (임포트)

1. **File → Open Projects from File System…** 선택
2. `Import source` 에서 이 폴더(`STM32F103_StdPeriph_W6100/`) 선택
3. 프로젝트 체크 후 **Finish**
4. **Project → Build Project** (Ctrl+B)

### 방법 B – 수동 설정 확인

`.cproject` 파일이 이미 아래를 포함하고 있지만,  
CubeIDE 버전 차이가 있을 경우 직접 확인하세요.

#### Include Paths
Project Properties → C/C++ Build → Settings → MCU GCC Compiler → Includes:
```
../Core/Inc
../BSP
../Drivers/StdPeriph/inc
../Drivers/CMSIS/CM3/CoreSupport
../Drivers/CMSIS/CM3/DeviceSupport/ST/STM32F10x
```

#### Preprocessor Defines
같은 설정 화면 → Preprocessor:
```
USE_STDPERIPH_DRIVER
STM32F10X_MD
DEBUG
```

#### Linker Script
MCU GCC Linker → General:
```
../STM32F103C8TX_FLASH.ld
```

#### Source Folders (빌드에 포함)
- `Core/Src`
- `BSP`
- `Drivers/StdPeriph/src`
- `startup`

---

## 핀 배치

| MCU 핀 | 기능 | 비고 |
|--------|------|------|
| PA4 | W6100 /CS (SPI NSS, SW) | Active-Low |
| PA5 | SPI1_SCK | |
| PA6 | SPI1_MISO | |
| PA7 | SPI1_MOSI | |
| PC13 | On-board LED | Active-Low (Blue Pill) |

---

## W6100 전체 드라이버 연동

이 템플릿의 `BSP/w6100.c` 는 최소 SPI 프레임 stub 입니다.  
WIZnet 공식 드라이버(`ioLibrary_Driver`)로 교체하려면 `BSP/w6100.c` 안의  
**"Integration note"** 주석을 참조하세요.

```
https://github.com/Wiznet/ioLibrary_Driver
```

---

## 주의사항

- HAL 라이브러리를 **사용하지 않습니다**. CubeMX 재생성 시 `Core/Src/main.c`가 덮어씌워지지 않도록 주의하세요.
- `system_stm32f10x.c` 도 CubeMX 버전이 아닌 StdPeriph 버전을 사용합니다.
- `startup_stm32f103c8tx.s` 는 레거시 어셈블리 포맷입니다. GCC ARM Toolchain 10 이상에서 정상 동작합니다.

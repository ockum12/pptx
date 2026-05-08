# Drivers/CMSIS

## 개요 (Overview)

이 폴더는 **ARM CMSIS CM3** 및 **STM32F10x 디바이스 지원** 파일을 담는 곳입니다.  
StdPeriph 라이브러리를 빌드하려면 아래 파일들이 필요합니다.

This folder holds the **ARM CMSIS CM3** and **STM32F10x device support** files  
required to build with the StdPeriph library.

---

## 필요한 폴더 구조 (Required folder structure)

```text
Drivers/CMSIS/
└── CM3/
    ├── CoreSupport/
    │   ├── core_cm3.c
    │   └── core_cm3.h
    └── DeviceSupport/
        └── ST/
            └── STM32F10x/
                ├── stm32f10x.h        ← main device header
                ├── system_stm32f10x.h ← system clock header
                └── startup/           ← (optional; we use startup/ at project root)
```

---

## 소스 구하는 방법 (How to obtain)

StdPeriph 패키지(`STM32F10x_StdPeriph_Lib_Vx.x.x.zip`)에 포함되어 있습니다.  
압축 해제 후:

```
Libraries/CMSIS/CM3/CoreSupport/       → Drivers/CMSIS/CM3/CoreSupport/
Libraries/CMSIS/CM3/DeviceSupport/ST/  → Drivers/CMSIS/CM3/DeviceSupport/ST/
```

위 경로로 복사하세요.

---

## 주요 파일 설명

| 파일 | 설명 |
|------|------|
| `core_cm3.h` | ARM Cortex-M3 CMSIS 코어 헤더 |
| `core_cm3.c` | Cortex-M3 인트린식 구현 (일부 컴파일러) |
| `stm32f10x.h` | STM32F10x 레지스터 맵 전체 정의 |
| `system_stm32f10x.h` | `SystemInit()` / `SystemCoreClockUpdate()` 선언 |

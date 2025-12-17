# SO2025-Grupo13
Alumno: Yamil Yaluk  
Repositorio para los TPs 1 y 2 de Sistemas Operativos 1 2025

# TP 1 -- LFS
## Descripción
Construcción de un sistema Linux mínimo desde cero, siguiendo el manual oficial de Linux From Scratch (versión 12.4) y utilizando systemd como sistema de inicialización.

El diario se encuentra en formato PDF en la carpeta docs.

## Contenidos
- **Estado del Arte**: revisión académica de los últimos 10 años sobre LFS y proyectos similares. Incluye tendencias actuales: optimización, control total, personalización y valor educativo
- **Instalación de LFS**: compilación y configuración de un sistema booteable, kernel y GRUB, con documentación de problemas y soluciones
- **Uso de Systemd como inicializador**: verificación como PID 1, gestión de servicios y logging centralizado con journald
- **Registro de Proceso**: Diario con los problemas y sus soluciones. Se encuentra en formato PDF

# TP 2 -- SHELL
## Descripción
Implementación de una **shell** básica con comandos propios, control de versiones y documentación técnica. El sistema está diseñado e implementado para funcionar tanto en Linux como en Windows.

Esta shell tiene un enfoque en seguridad con capacidades para restringir usos o capacidades según por ejemplo el horario. También tiene un fuerte sistema de logging con detalles para tener buena información de su uso. 

Otra particularidad es que la shell está disponible en español e inglés.

El diario se encuentra en formato PDF en la carpeta docs.

## Objetivos
- Construir un shell con características diferenciales (ej. educativo, de red, seguridad, minimalista, temático)
- Programar comandos desde cero, sin usar directamente los del sistema
- Mantener logs y documentación de decisiones, pruebas y problemas.

## Comandos implementados
- ls
- cd
- cp
- rm
- mkdir
- echo
- cat
- pwd
- exit
- curf (original)
- inputlimit (original)
- chlan (original)

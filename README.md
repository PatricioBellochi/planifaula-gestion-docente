# PlanifAula - Sistema de Gestión Docente (Avance 60%)
# Informe de Avance de Proyecto (60%) y Control de Versiones — PlanifAula

## Datos de la Entrega
* **Nombre del Informe:** Informe de Avance (60%), Gestión de Equipo Unipersonal y Control de Versiones — Sistema "PlanifAula"
* **Carrera:** Tecnicatura Universitaria en Sistemas de la Información (orientación Desarrollo Web)
* **Materia:** Taller de proyectos II
* **Fecha de entrega:** 17/11/2026
* **Enlace al proyecto (Repositorio GitHub):** (https://github.com/PatricioBellochi/planifaula-gestion-docente)

### Integrantes del Proyecto
* **Nombre y Apellido:** Patricio Tomas Bellochi
* **DNI:** 40718485
* **Correo electrónico:** bellochipatricio@gmail.com
* **Rol y participación:** 100% — Integrante único (modalidad de desarrollo *indie* asistido por Inteligencia Artificial).

---

## 1. Organización del Equipo, Planificación y Evaluación de Participación
Al igual que en proyectos previos de la carrera (*Grimorio Virtual*), este desarrollo se lleva adelante de manera **íntegramente individual**, sin otros integrantes humanos en el equipo. Dado el contexto real de cursar la etapa final de la tecnicatura mientras ejerzo simultáneamente cargos docentes activos, la gestión del tiempo y la planificación resultan críticas.

Para cumplir en tiempo y forma con cada etapa del ciclo de vida del software:
* **Aplicación de técnicas de planificación (Taller de Proyectos I):** Se aplicó descomposición de tareas (EDT/WBS) y planificación por hitos semanales (cronograma tipo Gantt en 3 iteraciones), priorizando en las primeras dos iteraciones el núcleo funcional (60%) para asegurar entregas ejecutables tempranas.
* **Dinámica de trabajo asistida por IA:** Asumo en solitario la totalidad de los roles decisorios (análisis funcional, arquitectura de datos, validación pedagógica, pruebas e integración en Git), utilizando herramientas de Inteligencia Artificial como copiloto técnico para acelerar la generación de código estructural (*boilerplate* en HTML/CSS y rutas CRUD).
* **Trazabilidad en Git:** La participación individual y el progreso incremental se encuentran auditados mediante *commits* cronológicos en la rama `main` del repositorio enlazado.

---

## 2. Estado de Avance del Proyecto (60% Completado)

| Iteración / Módulo | Tareas Planificadas | Estado | Avance | Evidencia en Git |
| :--- | :--- | :---: | :---: | :--- |
| **Iteración 1: Análisis y Diseño** | Relevamiento, diagramas de flujo (Eraser.io), prototipos UI (Figma) y modelado relacional. | Completado | 15% | Carpeta `/docs` |
| **Iteración 1: Base de Datos** | Implementación de entidades (`espacios_curriculares`, `unidades`, `clases`, `recursos`) y tabla intermedia N:M en SQLite. | Completado | 15% | Commit `feat(db)` |
| **Iteración 2: Backend CRUD** | Desarrollo en Python (Flask) de altas, consultas y cambio de estado de clases (*Planificada / Dictada / Reprogramada*). | Completado | 15% | Commit `feat(backend)` |
| **Iteración 2: Interfaz Web** | Construcción de vistas responsivas (*Dashboard* y *Detalle de Materia*) y vinculación de recursos didácticos. | Completado | 15% | Commit `feat(ui)` |
| **Iteración 3: Cierre (Pendiente)** | Reprogramación automática en cascada, exportación de planificación a PDF, login de usuario y pruebas finales. | Pendiente (Próximo módulo) | 0% (de 40%) | Planificado |
| **TOTAL ACUMULADO** | — | **En curso** | **60%** | **Rama `main` pública** |

---

## 3. Registro Preliminar de Pruebas y Mantenimiento Realizados
Siguiendo las buenas prácticas del ciclo de vida, se documentan las primeras verificaciones ejecutadas sobre el avance actual:
1. **Prueba de integridad relacional (SQLite):** Se verificó la creación automática de `planifaula.db` y el funcionamiento del borrado en cascada (`cascade="all, delete-orphan"`) al eliminar una unidad didáctica, confirmando que los materiales del banco general (`recursos`) permanecen intactos.
2. **Prueba funcional de flujo de clases:** Se comprobó el registro de espacios curriculares, creación de unidades y transición de estados de clase (*Planificada* -> *Dictada* / *Reprogramada*) con actualización inmediata en el contador del panel principal.
3. **Mantenimiento preventivo de repositorio:** Se configuró `.gitignore` para excluir archivos locales temporales (`__pycache__/`, `*.db`, `venv/`), manteniendo el repositorio limpio y portable.

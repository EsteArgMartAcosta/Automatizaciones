/**
 * Crea una reunión 1:1 con Google Meet para mardilao@unal.edu.co
 * Fecha: 1 de agosto de 2025, 13:00 hora Bogotá, duración 1 hora.
 * Ejecuta createMeetingForMardilao desde el editor.
 */
function createMeetingForMardilao() {
  try {
    const attendee = "mardilao@unal.edu.co";
    // Fecha y hora: 1 de agosto de 2025 a las 13:00 (Bogotá, -05:00), duración 60 minutos
    const start = new Date("2025-08-01T13:00:00-05:00");
    const end = new Date(start.getTime() + 60 * 60000); // +60 min

    const eventBody = {
      summary: "Reunión 1:1",
      description: "",
      start: { dateTime: start.toISOString() },
      end: { dateTime: end.toISOString() },
      attendees: [{ email: attendee }],
      conferenceData: {
        createRequest: {
          requestId: Utilities.getUuid(),
          conferenceSolutionKey: { type: "hangoutsMeet" }
        }
      }
    };

    // Crea el evento con Google Meet y envía la invitación
    const createdEvent = Calendar.Events.insert(eventBody, "primary", {
      conferenceDataVersion: 1
    });

    const meetLink = (createdEvent.conferenceData?.entryPoints || [])
      .find(ep => ep.entryPointType === "video")?.uri || "";

    Logger.log("✅ Reunión creada.");
    Logger.log("Enlace Meet: %s", meetLink);
    Logger.log("Evento en Calendar: %s", createdEvent.htmlLink);
  } catch (e) {
    Logger.log("❌ Error creando la reunión: %s", e.message);
  }
}


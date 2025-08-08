function createColoredFolders() {
  // ID de la carpeta donde se crearán las subcarpetas
  var parentFolderId = '1meX9ueJH7uuxMXph56T6RgRPcbuV4Tmn';
  
  // Obtener la carpeta padre en Google Drive
  var parentFolder = DriveApp.getFolderById(parentFolderId);
  
  // Crear nombres de carpetas de Semana 1 a Semana 16
  var folderNames = [];
  for (var i = 1; i <= 16; i++) {
    folderNames.push("Semana " + i);
  }

  // Lista de colores en formato RGB para cada carpeta
  var folderColors = [
    "#FF0000", "#00FF00", "#0000FF", "#FFFF00", "#FF00FF", "#00FFFF", "#FFA500", "#800080",
    "#808080", "#A52A2A", "#008000", "#000080", "#FFD700", "#DC143C", "#8B4513", "#4682B4"
  ];

  // Crear cada carpeta con su color correspondiente
  for (var i = 0; i < folderNames.length; i++) {
    var folder = parentFolder.createFolder(folderNames[i]); // Crear carpeta
    var folderId = folder.getId();
    
    var resource = {
      "folderColorRgb": folderColors[i] // Asignar color en formato RGB
    };

    // Usar Drive API para actualizar el color de la carpeta
    Drive.Files.update(resource, folderId);

    Logger.log('Carpeta creada: ' + folderNames[i] + ' con color ' + folderColors[i]);
  }
}


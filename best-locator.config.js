// best-locator.config.js
module.exports = {
  // Framework por defecto
  defaultFramework: 'playwright', // 'playwright' | 'cypress' | 'selenium'
  
  // Lenguaje por defecto
  defaultLanguage: 'typescript', // 'typescript' | 'javascript' | 'python'
  
  // Timeouts personalizados (en milisegundos)
  timeouts: {
    pageLoad: 30000,        // Tiempo para cargar página
    elementSelection: 60000, // Tiempo para seleccionar elementos
    validation: 15000       // Tiempo para validar selectores
  },
  
  // Estrategia de selectores (1 = prioridad más alta)
  selectorStrategy: {
    testAttributes: 1,      // data-testid, data-cy, data-test
    ids: 2,                 // #unique-id
    semanticAttributes: 3,  // name, role, aria-label
    textContent: 4,         // text="Button Text"
    cssClasses: 5          // .my-class
  },
  
  // Atributos específicos de tu proyecto
  projectAttributes: [
    'data-testid',
    'data-cy', 
    'data-test',
    'data-qa',              // Agrega tus atributos custom
    'data-automation'
  ],
  
  // Configuración del navegador
  browser: {
    headless: false,        // true para CI/CD
    viewport: {
      width: 1280,          // Ancho personalizado
      height: 720           // Alto personalizado
    },
    userAgent: undefined    // Custom user agent si necesitas
  },
  
  // Configuración de output
  output: {
    format: 'string',       // 'string' | 'object' | 'json'
    includeConfidence: true, // Mostrar porcentaje de confianza
    includeXPath: false,    // Incluir XPath alternativo
    autoSave: undefined     // './selectors' para auto-guardar
  },
  
  // URLs frecuentes del proyecto
  urls: {
    local: 'http://localhost:3000',
    dev: 'https://dev.myapp.com',
    staging: 'https://staging.myapp.com',
    prod: 'https://myapp.com'
  }
};
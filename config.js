/* ─────────────────────────────────────────────────────────────
   CONFIGURACIÓN — Di Trani, Almacén de Vinos (Viamonte 576, CABA).
   Los vinos y el almacén se cargan en la planilla: vinos.csv o una Google Sheet publicada.
   Lo marcado "A CONFIRMAR" sale de la muestra: hay que preguntárselo a Di Trani.
   ───────────────────────────────────────────────────────────── */
window.VINOTECA = {
  demo: false,
  nombre: 'Di Trani',
  barrio: 'San Nicolás',
  direccion: 'Viamonte 576',
  ciudad: 'Ciudad de Buenos Aires',
  mapa: 'https://www.google.com/maps/search/?api=1&query=Di+Trani+Almac%C3%A9n+de+Vinos+Viamonte+576+CABA',
  whatsapp: '5491164696600',
  instagram: 'ditrani.almacen',
  mail: '',                                     // A CONFIRMAR: no figura en IG ni en Maps
  // Horario del Instagram (bio). La hora de apertura del sábado no figura: A CONFIRMAR.
  horario: [['Lunes a viernes', '10 a 19:30 h'], ['Sábados', 'hasta las 18 h']],
  color: '#1a1412',                             // el negro del logo
  tinto: '#6e1f2b',                             // tapa de los tintos en la caja
  rating: '5,0',
  resenas: 64,

  planilla: '',

  caja: { botellas: 6, descuento: 10 },        // A CONFIRMAR: el % por caja completa es de ejemplo
  // Envoltorios: la caja de pino grabada es la de sus posteos. Precios A CONFIRMAR (null = "a confirmar").
  regalo: [
    ['Caja de pino grabada, 1 botella', null],
    ['Caja de pino grabada, 2 botellas', null],
    ['Bolsa de regalo', null],
  ],
  extras: ['Copa grabada', 'Chocolate', 'Aceite de oliva', 'Picada (salame y mermelada)'],
  // Instagram: "Envíos por CABA y GBA (consultar zonas)". Costos y días A CONFIRMAR.
  envios: [
    ['Retiro en Viamonte 576', 0, 'cuando quieras, en horario del local'],
    ['Microcentro y San Nicolás', null, 'consultá costo y día por WhatsApp'],
    ['Resto de CABA', null, 'consultá costo y día por WhatsApp'],
    ['GBA', null, 'consultá zonas por WhatsApp'],
  ],
  envioGratisDesde: 0,
  pagos: ['A coordinar por WhatsApp'],       // A CONFIRMAR: medios de pago (placeholder visible a propósito) taste-skill-ignore
  pagosPendiente: true,
};

export const API_BASE_DEV = 'http://localhost:5000/';
export const API_BASE_PRD = 'http://api.gtszoffice.com/';
export const API_BASE = process.env.NODE_ENV == 'development' ? API_BASE_DEV : API_BASE_PRD

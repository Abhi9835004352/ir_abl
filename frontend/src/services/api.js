import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
    baseURL: API_BASE_URL,
    headers: {
        'Content-Type': 'application/json',
    }
});

export const searchService = {
    search: async (query) => {
        try {
            const response = await api.get('/search', { params: { query } });
            return response.data;
        } catch (error) {
            console.error('Search error:', error);
            throw error;
        }
    },

    logClick: async (urlId) => {
        try {
            const response = await api.post('/click', { url_id: urlId });
            return response.data;
        } catch (error) {
            console.error('Click logging error:', error);
            throw error;
        }
    }
};

export default api;

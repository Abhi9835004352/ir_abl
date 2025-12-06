import React, { useState } from 'react';
import SearchBar from '../components/SearchBar';
import ResultCard from '../components/ResultCard';
import { searchService } from '../services/api';
import '../styles/ResultsPage.css';

const ResultsPage = () => {
    const [results, setResults] = useState([]);
    const [loading, setLoading] = useState(false);
    const [query, setQuery] = useState('');
    const [error, setError] = useState('');

    const handleSearch = async (searchQuery) => {
        setQuery(searchQuery);
        setLoading(true);
        setError('');
        setResults([]);

        try {
            const data = await searchService.search(searchQuery);
            setResults(data);

            if (data.length === 0) {
                setError('No results found. Try a different search.');
            }
        } catch (err) {
            setError('An error occurred while searching. Please try again.');
            console.error('Search error:', err);
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="results-page">
            <div className="header">
                <h1>🔍 Intelligent Search Engine</h1>
                <p>Powered by TF-IDF + SEO + Popularity Ranking</p>
            </div>

            <SearchBar onSearch={handleSearch} loading={loading} />

            {loading && (
                <div className="loading">
                    <div className="spinner"></div>
                    <p>Fetching and ranking results...</p>
                </div>
            )}

            {error && <div className="error">{error}</div>}

            {results.length > 0 && (
                <div className="results-container">
                    <div className="results-header">
                        <h2>Results for "{query}"</h2>
                        <p className="result-count">Found {results.length} results</p>
                    </div>

                    <div className="results-list">
                        {results.map((result, index) => (
                            <div key={result.url_id} className="result-wrapper">
                                <span className="result-number">{index + 1}</span>
                                <ResultCard result={result} />
                            </div>
                        ))}
                    </div>
                </div>
            )}

            {!loading && !error && results.length === 0 && (
                <div className="welcome">
                    <h2>Welcome to Intelligent Search Engine</h2>
                    <p>Start by entering a search query above</p>
                </div>
            )}
        </div>
    );
};

export default ResultsPage;

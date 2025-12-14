import React from 'react';
import '../styles/ResultCard.css';
import { searchService } from '../services/api';

const ResultCard = ({ result }) => {
    const handleClick = async (e) => {
        e.preventDefault();
        try {
            await searchService.logClick(result.url_id);
        } catch (error) {
            console.error('Failed to log click:', error);
        }
        window.open(result.url, '_blank');
    };

    const getScoreColor = (score) => {
        if (score >= 0.8) return '#27ae60';      // Green
        if (score >= 0.6) return '#f39c12';      // Orange
        if (score >= 0.4) return '#e74c3c';      // Red
        return '#95a5a6';                        // Gray
    };

    const getScorePercentage = (score) => {
        return Math.round(score * 100);
    };

    return (
        <div className="result-card">
            <div className="result-header">
                <h3 className="result-title">{result.title || 'No Title'}</h3>
                <a
                    href={result.url}
                    className="result-url"
                    target="_blank"
                    rel="noopener noreferrer"
                >
                    {result.url}
                </a>
            </div>

            <p className="result-description">
                {result.meta_description || 'No description available'}
            </p>

            <div className="result-metrics">
                {/* <div className="metric">
                    <span className="metric-label">Relevance:</span>
                    <span className="metric-value">
                        {getScorePercentage(result.relevance_score)}%
                    </span>
                </div> */}

                <div className="metric">
                    <span className="metric-label">SEO Score:</span>
                    <div className="score-bar-container">
                        <div
                            className="score-bar"
                            style={{
                                width: `${result.meta_score}%`,
                                backgroundColor: getScoreColor(result.meta_score / 100)
                            }}
                        ></div>
                    </div>
                    <span className="metric-value">{Math.round(result.meta_score)}/100</span>
                </div>

                <div className="metric">
                    <span className="metric-label">Popularity:</span>
                    <span className="metric-value">
                        {getScorePercentage(result.popularity_score)}%
                    </span>
                </div>

                <div className="metric">
                    <span className="metric-label">Final Score:</span>
                    <span className="metric-value" style={{ fontWeight: 'bold' }}>
                        {getScorePercentage(result.final_score)}%
                    </span>
                </div>
            </div>

            <button
                className="visit-button"
                onClick={handleClick}
            >
                Visit Website
            </button>
        </div>
    );
};

export default ResultCard;

function LoadingStatus ({theme}) {
    return (
        <div className="loading-container">
            <h2>Generating your story on the topic {theme}</h2>
            <div className="loading-animation">
                <div className="spinner"></div>
            </div>
            <p className="loading-info">
                Pleae wait while we create a unique and engaging story for you...
            </p>
        </div>
    )
}

export default LoadingStatus
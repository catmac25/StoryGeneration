import { useState } from "react"

function ThemeInput({onSubmit}) {
    const [theme, setTheme] = useState("")
    const [error, setError] = useState("")
    const handleSubmit = (e) => {
        e.preventDefault();

        if (!theme.trim()) {
            setError("Please enter a theme name");
            return
        }

        onSubmit(theme);
    }
    return (
        <div className="mt-10">
        <div className="theme-input-container">
            <h2>Generate Your Adventure</h2>
            <p>Enter a topic for your story</p>

            <form onSubmit={handleSubmit}>
                <div className="input-group">
                    <input type="text" value={theme}
                        onChange={(e) => setTheme(e.target.value)}
                        placeholder="enter the topic prompt"
                        className={error ? 'error' : ''} />

                    {error && <p className="error-text">{error}</p>}
                </div>
                <button type="submit" className="generate-btn">
                    Generate Story
                </button>
            </form>
        </div>
        </div>
    )
}

export default ThemeInput
import {useState, useEffect} from "react"
import {useNavigate} from "react-router-dom"
import LoadingStatus from "../components/LoadingStatu"
import ThemeInput from "./ThemeInput"
const API_BASE_URL = "/api"

function StoryGenerator() {
    const navigate = useNavigate()
    const [prompt, setPrompt] = useState("")
    const [error, setError] = useState(null)
    const [loading, setLoading] = useState(false)

    const generateStory= async(prompt) => {
        setLoading(true)
        setError(null)
        setPrompt(prompt)

        try{
            const response = await fetch(`${API_BASE_URL}/stories/create`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({prompt})
            })
            if (!response.ok) {
                throw new Error("Failed to generate story");
            }

            const data = await response.json();
            navigate(`/stories/${data.id}`)
        }catch(err){
            console.error("Error generating story:", err);
      setError("Could not generate story. Please try again.");
        }finally{
            setLoading(false)
        }

        
    }
    return (
        <div className="story-generator">
  <h2 className="mb-20">Generate a Story</h2>

  <ThemeInput onSubmit={generateStory}/>

  {loading && <LoadingStatus message="Creating your story..." />}
  {error && <p className="error">{error}</p>}
</div>
    )
}

export default StoryGenerator
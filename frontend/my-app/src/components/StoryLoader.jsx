import { useState, useEffect } from "react";
import {useParams, useNavigate} from "react-router-dom"
import LoadingStatus from "../components/LoadingStatu"

const API_BASE_URL = "/api"

function StoryLoader(){
    const [story, setStory] = useState(null);
    const [loading, setLoading]= useState(true);
    const [error, setError] = useState(null);
    const navigate = useNavigate();
    const {id} = useParams();
    
    useEffect(()=> {
        loadStory(id)
    }, [id]);

    const loadStory = async(storyId) => {
        setLoading(true)
        setError(null);

        try{
            const response = await fetch(`${API_BASE_URL}/stories/${storyId}/complete`);
            if (!response.ok){
                throw new Error (`Error: ${response.status} ${response.statusText}`);
            }
            const data = await response.json();
            setStory(data);

        }catch(err){
            console.log("Error occurred while fetching story", err);
            setError("Failed to load story. Please try again later.");
        }finally{
            setLoading(false)
        }
    }

   if (error){
    return (
        <div>
            <h1> {error}</h1>
            <button onClick={() => navigate('/')}> Go to Story Generator</button>
        </div>
    )
   }
   if (loading){
    return <LoadingStatus message="Loading your story..." />
   }

   return (
    <div className="story-container">
        <h2>Topic: {story.prompt}</h2>
      <p>{story.generated_story}</p>
      <small>Created at: {new Date(story.created_at).toLocaleString()}</small>
      <p className="font-light text-green-400">story fetched successfully</p>
    </div>
   )
}
export default StoryLoader
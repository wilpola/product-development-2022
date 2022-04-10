import { useEffect, useState } from "react"


const MainCard = (id, image, name, title, content="", info="") => {
    const [data, setData] = useState({})

    useEffect(() => {
        setData({
            id: id,
            name: name
        })
    }, [])
    return (
        <div id="mainCard-container"> 
            <h2>#{data.name}</h2>
        </div>
    )
}
export default MainCard;
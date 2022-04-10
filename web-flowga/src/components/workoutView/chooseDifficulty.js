import React from 'react';


const ChooseDifficulty = (difficulty) => {

    const handleClick =(e) =>{
        e.preventDefault();
        difficulty = e.target.innerHTML;
        console.log(e.target.innerHTML) 
    }

    return (
        <div className="difficultySeelctor-container">
            <h1> Choose workout difficulty</h1>
            <button onClick={(e) => handleClick(e)}>Easy</button>
            <button onClick={(e) => handleClick(e)}>Medium</button>
            <button onClick={(e) => handleClick(e)}>Hard</button>
        </div>
    )
}
export default ChooseDifficulty;
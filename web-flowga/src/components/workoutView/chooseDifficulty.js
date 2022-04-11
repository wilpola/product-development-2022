import React from "react";
import { DifficultyCard } from "../flowga-app/card";

const ChooseDifficulty = (difficulty) => {
  const handleClick = (e) => {
    e.preventDefault();
    difficulty = e.target.innerHTML;
    console.log(e.target.innerHTML);
  };

  return (
    <div className='difficultySelector-container'>
      <h1> Choose workout difficulty</h1>
      <div className='diff-cards'>
        <DifficultyCard img='easy.png' title='Easy' className='easy' />
        <DifficultyCard img='medium.png' title='Medium' className='medium' />
        <DifficultyCard img='hard.png' title='Hard' className='hard' />
      </div>
    </div>
  );
};
export default ChooseDifficulty;

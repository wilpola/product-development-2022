import React, {useState, useEffect } from 'react';
import ChooseDifficulty from './chooseDifficulty';
import MainCard from './mainCard';
import './workout.scss';

const Workout = () => {
    const [difficulty, setDifficulty ] = useState();

    return (
        <div className='workout-container'>
            <ChooseDifficulty difficulty={difficulty} />
            {difficulty}
            <MainCard id='1' name="asana"/>
        </div>
    )
}
export default Workout;
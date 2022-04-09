import React from 'react';
import YogaLanding from '../../assets/img/yoga-landing.svg';
import './home.scss';

const Home = () => {
    return(
        <div className='home-container'>
            <section id="landing">
                <img src={YogaLanding} alt=''/>
            </section>
        </div>
    )
}
export default Home;
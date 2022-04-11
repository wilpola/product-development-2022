import React from "react";
import { Link } from "react-router-dom";
import YogaLanding from "../../assets/img/yoga-landing.svg";
import FamilyIcon from "../../assets/img/family.png";
import GlobeIcon from "../../assets/img/globe.png";
import ProgressIcon from "../../assets/img/progress.png";
// import Amk from "../../assets/img/amk.jpg";
import { Footer } from "../index";
import "./home.scss";
import { DifficultyCard } from "../flowga-app/card";

const Home = () => {
  return (
    <div className='home-container'>
      <section id='landing'>
        {/* <div className='landing-content'> */}
        <h1 className='landing-header'> Connect with your body</h1>
        <p className='landing-body'>
          Flowga is a yoga app that will generate a semi-randomized yoga
          workouts based on selected parameters. Stay in shape even when gyms
          are closed.
        </p>
        <div className='callToAction'>
          <Link className='btn' to='/flowga-app'>
            Try Flowga
          </Link>
          <Link to='/documentation' className='learn-more'>
            {" "}
            Learn More{" "}
          </Link>
        </div>
        {/* </div> */}
        <div className='landing-image'>
          <img src={YogaLanding} alt='' />
        </div>
      </section>
      <section id='information'>
        <div className='modern-back' />
        <h2> What makes Flowga so great</h2>
        <p className='info-content'>
          At Meddler Labs, we believe that sound mind and body helps us work
          more efficiently, and the quality of our work is better. Thus, we have
          build a yoga app that helps your developers stay healthy, and more
          focused.
        </p>
        <div className='information-banner'>
          <div>
            <img src={FamilyIcon} />
            <h2>Made for Everyone</h2>
            <p>
              {" "}
              Flowga allows the user the select the difficulty of their workout
              to suit their current abilities in yoga.
            </p>
          </div>
          <div>
            <img src={GlobeIcon} />
            <h2> Workout anywhere</h2>
            <p>
              {" "}
              Flowga is accessible from anywhere at any time. In the case that
              you device is not connected to the internet, the workouts get
              stored onto the device, until they can be synced with your cloud
              data.
            </p>
          </div>
          <div>
            <img src={ProgressIcon} />
            <h2> Track progress </h2>
            <p>
              {" "}
              Workouts get stored, in the cloud to allow you to look back how
              you have progressed. See your past workouts, and be motivated by
              your workout streak.
            </p>
          </div>
        </div>
      </section>
      <section id='about'>
        <div className='blur-container' />
        <div className='cta-container'>
        <h3> About Meddler Labs</h3>
            <p>
             Meddler Labs is a group of students from Product Development course in Turku University of Applied Sciences. As a part of a semester long assingment to build an application of our choise, we decided to that building a Yoga application would nott only be exciting, but also fill a need in the world...
            </p>
          <div className='download__learn-more-container'>
            <Link to='/about'>Read more</Link>
          </div>
        </div>
      </section>
      <section id='download-meddler'>
        <div className='meddler-inner-container'>
          <div className='blur-container' />
          <div className='meddler-img' />
          <div className='cta-container'>
            <h3> Download our Desktop version</h3>
            <p>
              Our desktop version is written in Python, and can be downloaded
              for windows, macOS, or Linux.
            </p>
            <div className='download__learn-more-container'>
              <button> Download </button>
              <Link to='/download'>Learn more</Link>
            </div>
          </div>
        </div>
      </section>
      <Footer />
    </div>
  );
};
export default Home;

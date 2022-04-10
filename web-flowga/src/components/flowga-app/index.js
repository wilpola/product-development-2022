import React, { useState, useEffect } from "react";
import nextId from "react-id-generator";

import Confirm from "../Confirm";

// import styles
import "./flowga-app.scss";

const FlowgaApp = () => {
  const [username, setUsername] = useState("");
  const [formError, setFormError] = useState(false);
  const [workouts, updateWorkouts] = useState([]);
  const [confirm, setConfirm] = useState(false);

  let ids = nextId();

  const time = new Date();
  //   console.log(time.toLocaleDateString("default", { dateStyle: "short" }));
  let flowData = {
    username: "",
    lastLogin: time.toLocaleDateString("default", { dateStyle: "short" }),
    workouts: [],
  };

  const cap = (t) => {
    return t.charAt(0).toUpperCase() + t.substr(1).toLowerCase();
  };

  let data = JSON.parse(localStorage.getItem("flowga-app"));
  let state = false;
  data === null ? (state = false) : (state = true);

  useEffect(() => {
    if (data === null) {
      state = false;
    } else {
      setUsername(data.username);
      updateWorkouts(data.workouts);
      state = true;
    }
  }, [state]);

  const handleSubmit = (e) => {
    e.preventDefault();
    let x = document.getElementById("usernameField");
    if (x.value === "") {
      x.classList.add("err");
      setFormError(true);
    } else {
      setUsername(x.value);
      flowData.username = x.value;
      localStorage.setItem("flowga-app", JSON.stringify(flowData));
    }
  };

  if (state === false) {
    return (
      <div className='FirstTime-container'>
        <form className='userForm-container' onSubmit={(e) => handleSubmit(e)}>
          <h1> Enter your username:</h1>
          {formError ? (
            <p
              style={{
                color: "#ff0000",
                marginBottom: "-10px",
                padding: "none",
              }}
            >
              * Please enter a username
            </p>
          ) : null}
          <input
            id='usernameField'
            placeholder='Username'
            autoComplete='off'
            required
            onFocus={() =>
              document.getElementById("usernameField").classList.add("focused")
            }
            onBlur={() =>
              document
                .getElementById("usernameField")
                .classList.remove("focused")
            }
          />{" "}
          <br />
          <button onClick={(e) => handleSubmit(e)} type='submit'>
            {" "}
            Login{" "}
          </button>
        </form>
      </div>
    );
  } else {
    // if userExists
    const time = new Date();

    let greeting = "";
    // console.log(time.toLocaleString("default", { dayPeriod: "narrow" }));

    if (
      time.toLocaleString("default", { dayPeriod: "narrow" }) === "at night"
    ) {
      greeting = "Hello, ";
    } else if (
      time.toLocaleString("default", { dayPeriod: "narrow" }) ===
      "in the afternoon"
    ) {
      greeting = "Good afternoon, ";
    } else {
      greeting = "Good morning, ";
    }

    const addworkout = () => {
      //data
      let d = JSON.parse(localStorage.getItem("flowga-app"));
      //dateTIME
      let t = new Date();
      console.log(t.toISOString());
      console.log(ids);

      function getDiff() {
        let num = Math.floor(Math.random() * 3);
        if (num === 1) {
          return "medium";
        } else if (num > 1) {
          return "hard";
        } else {
          return "easy";
        }
      }

      let w = {
        id: ids,
        title: "Afternoon workout",
        t: t,
        diff: getDiff(),
        length: Math.round(Math.random() * (1000 - 50) + 50),
        notes: "Everything was fine",
      };
      d.workouts.unshift(w);

      updateWorkouts((prevState) => [w, ...prevState]);
      let newEntry = data.workouts.unshift(w);

      localStorage.setItem("flowga-app", JSON.stringify(data));
    };

    const DateChange = (date) => {
      let d = date;
      let t = new Date(d);
      console.log(t.toLocaleDateString("default", { dateStyle: "short" }));
      return t.toLocaleDateString("default", { dateStyle: "short" });
    };
    return (
      <div className='flowga-app-container'>
        {/* <button
          onClick={() =>
            {
              let x = document.getElementsByClassName('confirm-outer').item(0).classList;
              x.add("vis");
              console.log(x)
            }
          }
        >
          SURPRISE
        </button> */}

        <div id='app-content'>
          <h2 className='greeting'> {greeting + cap(username)} </h2>
          <div className='activity-container'>
            <h3 className='recent-activity'> Recent activity</h3>
            <button onClick={() => addworkout()}> click me</button> <br />
            {workouts.length > 0
              ? workouts.map((item, index) => {
                  const addClass = (x) => {
                    if (x === "easy") {
                      return <p className='act-difficulty easy'>{item.diff}</p>;
                    } else if (x === "medium") {
                      return (
                        <p className='act-difficulty medium'>{item.diff}</p>
                      );
                    } else {
                      return <p className='act-difficulty hard'>{item.diff}</p>;
                    }
                  };
                  const confirmation = () => {
                    let x = document
                    .getElementsByClassName("confirm-outer")
                    .item(0).classList;
                    x.add("vis");

                    if (confirm === true) {
                      return true;
                    } else {
                      return false;
                    }
                  };

                  const removeWorkout = (e) => {
                    confirmation();
                    if (confirmation === true) {
                      const z = e.target.parentNode.getAttribute("name");
                      console.log(z);
                      
                      // console.log(x);
                      
                      data.workouts = workouts.filter((i) => i.id !== z);
                      updateWorkouts(workouts.filter((i) => i.id !== z));
                      
                      setTimeout("", 500);
                      
                      localStorage.setItem("flowga-app", JSON.stringify(data));
                    }
                  };

                  return (
                    <div
                      key={index}
                      name={item.id}
                      className='act-card'
                      onClick={(e) => removeWorkout(e)}
                    >
                      <h3>{item.title}</h3>
                      {addClass(item.diff)}
                      <p>{DateChange(item.t)}</p>
                    </div>
                  );
                })
              : ""}
          </div>
        </div>
        <Confirm />
      </div>
    );
  }
};

export default FlowgaApp;

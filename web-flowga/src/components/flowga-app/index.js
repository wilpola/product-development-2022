import React, { useState, useEffect } from "react";

// import styles
import "./flowga-app.scss";

const FlowgaApp = () => {
  const [username, setUsername] = useState("");
  const [formError, setFormError] = useState(false);

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
    console.log("first Time");
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
    let greeting = '';
    console.log(time.toLocaleString('default', {dayPeriod: 'narrow'}));

    if (time.toLocaleString('default', {dayPeriod: 'narrow'}) === "at night") {
      greeting = "Hello, "
    } else if (time.toLocaleString('default', {dayPeriod: 'narrow'}) === "in the afternoon") {
      greeting = "Good afternoon, "
    } else {
      greeting = "Good morning, "
    }
    return (
      <div className='flowga-app-container'>
        <h2> {greeting + cap(username)} </h2>
      </div>
    );
  }
};

export default FlowgaApp;

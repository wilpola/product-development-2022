import React, { useState, useEffect } from "react";

const FlowgaApp = () => {
  const [username, setUsername] = useState("");

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
  data === null ? state = false : state = true;

  useEffect(() => {
    //   setUsername(data.username);
      if (data === null) {
              state = false
        } else {
              setUsername(data.username);
              state = true
          }
  }, [state]);

  const handleSubmit = (e) => {
    e.preventDefault();
    let x = document.getElementById("usernameField").value;

    setUsername(x);
    flowData.username = x;
    localStorage.setItem("flowga-app", JSON.stringify(flowData));
  };

  if (state === false) {
    console.log("first Time");
    return (
      <div>
        <form onSubmit={(e) => handleSubmit(e)}>
          <input id='usernameField' placeholder='Username' />
          <button onClick={(e) => handleSubmit(e)}> Login </button>
        </form>
      </div>
    );
  } else {
    // if userExists
    return (
      <div className='flowga-app-container'>
        <h2> Welcome back, {cap(username)} </h2>
      </div>
    );
  }
};

export default FlowgaApp;

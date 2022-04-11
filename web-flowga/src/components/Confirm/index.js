import React, { useState } from 'react';
import "./confirm.scss";

function Confirm(props) {

    const [workouts, setWorkouts] = useState(props.data.workouts);

  const onConfirm = () => {
    console.log("Confirm");
    

        setWorkouts(workouts.filter((i) => i.id !== props.z));
        props.data.workouts = workouts;
        localStorage.setItem('flowga-app', JSON.stringify(props.data));

        document
        .getElementsByClassName("confirm-outer")
        .item(0)
        .classList.remove("vis");
        
  };
  const onCancel = () => {
    console.log("Cancel");
    document
      .getElementsByClassName("confirm-outer")
      .item(0)
      .classList.remove("vis");

  };
  const handleClick = (e) => {
    //   console.log(e.target.classList)
    let targ = e.target.classList;
    if (targ.contains("vis")) {
      document
        .getElementsByClassName("confirm-outer")
        .item(0)
        .classList.remove("vis");
    }
  };

  let state = "";

  return (
    <div className='confirm-outer' onClick={(e) => handleClick(e)}>
      <div className='confirm-container'>
        <h2 className='confirm-title'>This item will be permanently deleted</h2>
        <p className='confirm-body'>
          {`The following workout will be permanently deleted `} <br />{" "}
          {/* {`${item.title}`} */}
          <br />
          {/* {`${item.diff}`} */}
        </p>
        <div className='confirm-buttons'>
          <div className='btn confirm' onClick={() => onConfirm()}>
            <p>Confirm</p>
          </div>
          <div className='btn cancel' onClick={() => onCancel()}>
            <p>Cancel</p>
          </div>
        </div>
      </div>
    </div>
  );
};
export default Confirm;

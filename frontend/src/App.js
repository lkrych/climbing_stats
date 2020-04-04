import React, { useState, useEffect } from "react";

export default () => {

  let [count, setCount] = useState(0);



  return (
    <>
      <h1>Welcome to React Parcel Micro App!</h1>
      <p>Hard to get more minimal than this React app.</p>
      <p>Counter: {count}</p>
      <button onClick={() => setCount(count + 1)}>Increment</button>
    </>
  ) 
};

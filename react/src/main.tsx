import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'
import classes from "./style.module.css"
import Profile from './Profile'
import { useState } from 'react'

function Mycomponent (){
  const name = "Nac";
  const className = "heading";

  function formatName(name: string){
    return "Mr." + name;
  }

  const people = [
    {name: "Nac", age: 18, isSmart: true },
    {name: "Nene", age: 17, isSmart: true },
  ];
  const peopleElement = people.map( function(person) {
    return(
      <Profile
      key={person.name}
      name={person.name}
      age={person.age}
      isSmart={person.isSmart}
      />
    );
  });

  const myStyle = {
    color: "blue",
    backgroundColor: "red",
  };
  
  const [isOpen, setIsOpen] = useState(false);
  const [color, setColor] = useState("red");
  const [counter, SetCounter ] = useState(0); 
  function handleClick() {
    setIsOpen(function (prev){
      return !prev;
    });
    setColor(function (prev) {
      if (prev=='blue') return 'red';
      return 'cyan';
    });
    SetCounter(counter + 1);
  }

  return (
  <div> 
    
    <Profile name="Nac" age={18} isSmart />
    {peopleElement}
    <h1 className={className}> Hello </h1> 
    <p className={classes.heading1}> 
      {formatName(name)} 
    </p>

    <h3>{isOpen ? "Open" : "Disabled"}</h3>
    <button onClick={handleClick} style={{backgroundColor: color}}> 
      Press Me
    </button>
    <h3> {counter} Pressed </h3>
  </div>);
}




ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <Mycomponent/>
    <Mycomponent/>
    <App />
  </React.StrictMode>
)

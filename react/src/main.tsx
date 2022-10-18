import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'
import classes from "./style.module.css"


interface ProfileProps {
  name: string
  age: number
  isSmart?: boolean
}
function Profile (props: ProfileProps) {
  const { name, age, isSmart=false } = props;

  return (
  <p>
    {name} - {age} - {isSmart}
  </p>);
}

function Mycomponent (){
  const name = "Nac";
  const className = "heading";
  function formatName(name: string){
    return "Mr." + name;
  }

  const myStyle = {
    color: "blue",
    backgroundColor: "red",
  };
  return (
  <div> 
    <Profile name="Nac" age={18} isSmart />
    <h1 className={className}> Hello </h1> 
    <p style={myStyle}> 
      {formatName(name)} 
    </p>
   
  </div>);
}


ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <Mycomponent/>
    <App />
  </React.StrictMode>
)

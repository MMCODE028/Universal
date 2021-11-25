import React from "react";
import Perfil from "./Perfil.js";

import imagen1 from "../assets/imagen1.jpg";
import imagen2 from '../assets/imagen2.jpg';
import imagen3 from '../assets/imagen3.jpg';


const perfiles = [
  {
    id: 1,
    title: "Avianca",
    image: imagen1,
    url: "https://faztweb.com",
  },
  {
    id: 2,
    title: "Viva Colombia",
    image: imagen2,
    url: "https://blog.faztweb.com",
  },
  
  {
    id: 2,
    title: "American Airlanes",
    image: imagen3,
    url: "https://blog.faztweb.com",
  },
  
];

function Perfiles() {
  return (
    <div className="container d-flex justify-content-center align-items-center h-100">
      <div className="row">
        {perfiles.map(({ title, image, url, id }) => (
          <div className="col-md-4" key={id}>
            <Perfil imageSource={image} title={title} url={url} />
          </div>
        ))}
      </div>
    </div>
  );
}

export default Perfiles;
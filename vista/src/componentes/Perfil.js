import React from "react";
import PropTypes from "prop-types";

import "./Perfil.css";

function Perfil({ imageSource, title, text, url }) {
  return (
    <div className="perfil text-center bg-dark animate__animated animate__fadeInUp">
      <div className="overflow">
        <img src={imageSource} alt="a wallpaper" className="card-img-top" />
      </div>
      <div className="perfil-body text-light">
        <h4 className="perfil-title">{title}</h4>
        <p className="perfil-text text-secondary">
          {text
            ? text
            : ""}
        </p>
        <a
          href={url ? url : "#!"}
          target="_blank"
          className="btn btn-outline-secondary border-0"
          rel="noreferrer"
        >
          Ingresar {title}
        </a>
      </div>
    </div>
  );
}

Perfil.propTypes = {
  title: PropTypes.string.isRequired,
  text: PropTypes.string,
  url: PropTypes.string,
  imageSource: PropTypes.string
};

export default Perfil;
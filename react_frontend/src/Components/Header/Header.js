import React from "react";
import { useHistory } from "react-router";
import Logo from "../MenuItems/assets/card_images/final/logo.ico";
import "./Header.css";
import { Link } from "react-router-dom";
import axiosInstance from "../../axios";

export const Header = (props) => {
  const history = useHistory();

  const handleLogOut = () => {
    axiosInstance.post("/user/logout/");
    localStorage.removeItem("token");
    history.push("/");
  };

  return (
    <header className="navbar">
      <div
        className="navbar__title navbar__item"
        onClick={() => history.push("/home")}
      >
        <img
          alt="Baler Logo amar"
          src={Logo}
          width="80px"
          height="80px"
          style={{ borderRadius: "70px" }}
        ></img>
      </div>

      <div className="navbar__item" style={{ fontWeight: "bold" }}>
        {/* <Link to="/landingpage">Logout</Link> */}
        {/* <p onClick={handleLogOut}>Log out</p> */}
        {localStorage.length === 0 ? (
          <p onClick={() => history.push("/login")}>Log In</p>
        ) : (
          <p onClick={handleLogOut}>Log out</p>
        )}
      </div>
    </header>

    //   <Navbar className='header'>
    //   <Navbar.Body>
    //     <Nav>
    //       <Nav.Item icon={<Icon icon="home" />} onSelect={() => history.push('/')}> Home</Nav.Item>
    //     </Nav>
    //     <Nav pullRight>
    //       <Nav.Item >Login</Nav.Item>
    //     </Nav>
    //   </Navbar.Body>
    // </Navbar>
  );
};

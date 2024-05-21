import React from 'react';
import { useHistory } from 'react-router';
import './MenuItem.scss';

const MenuItem = (props) => {
    const {title, img, path} = props.menu;
    const history = useHistory();
    return (
        <div className=' menu-item' onClick={() => history.push(path)}>
        <div style={{backgroundImage:`url(${img})`}} 
        className="background-img"/>
        <div className="card content">
            <h1 className='title'>{title.toUpperCase()}</h1>
            <span className='subtitle'>CHECK NOW</span>
        </div>
        </div>
    );
};

export default MenuItem;
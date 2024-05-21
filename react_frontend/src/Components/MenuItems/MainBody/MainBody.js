import React from 'react';
import MenuItem from '../MenuItem';
import './MainBody.scss';
import random_disease_image  from '../assets/card_images/final/random-disease.jpeg';
import heart_disease_image from '../assets/card_images/final/heart.jpeg'
import diabetes_image from '../assets/card_images/final/diabetes.jpg';
import brest_cancer_image from '../assets/card_images/final/breast_cancer.jpeg';
import skin_cancer_image from '../assets/card_images/final/skin-cancer.jpeg';
import lung_cancer_image from '../assets/card_images/final/lung_cancer.png';

const MainBody = () => {
    const menus = [
        {id: 1, title: 'Random Disease Prediction', img: random_disease_image, path: '/random-disease-detection'},
        {id: 2, title: 'Heart Disease Prediction', img: heart_disease_image, path: '/heart-disease-detection'},
        {id: 3, title: 'Diabetes Prediction', img: diabetes_image, path: '/diabetes-detection'},
        {id: 4, title: 'Breast Cancer Prediction', img: brest_cancer_image, path: '/breast-cancer-detection'},
        {id: 5, title: 'Skin Cancer Prediction', img: skin_cancer_image, path: '/skin-cancer-detection'},
        {id: 6, title: 'Lung Cancer Prediction', img: lung_cancer_image, path: '/lung-cancer-detection'}
    ]

    return (
        <div className='main-body'>
            {menus.map((menu) => <MenuItem key={menu.id} menu={menu}></MenuItem>)}
        </div>
    );
};

export default MainBody;
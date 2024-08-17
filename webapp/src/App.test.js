import React from 'react';
import ReactDOM from 'react-dom';
import Appcon from './Appcon';

it('renders without crashing', () => {
  const div = document.createElement('div');
  ReactDOM.render(<Appcon />, div);
  ReactDOM.unmountComponentAtNode(div);
});

import React, { Component } from 'react';
import { Jsme } from 'jsme-react';
import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection
} from "streamlit-component-lib";


export class App extends StreamlitComponentBase {
  constructor(props) {
    super(props);
    this.state = {
      smiles: this.props.args["smiles"]
    };
    this.logSmiles = this.logSmiles.bind(this);
  }

  logSmiles(smiles) {
    console.log(smiles);
    Streamlit.setComponentValue({ data: { smiles: smiles } });
  }

  render() {
    const { smiles } = this.state;

    return (
      <div height="400px" width="550px">
        <Jsme
          height="350px"
          width="500px"
          smiles={smiles}
          options="oldlook,star"
          onChange={this.logSmiles}
        />
      </div>
    );
  }
}

export default withStreamlitConnection(App);

{
  /* comments are like this */
}

const JSX = (
  <div>
    <h1>
      Need every HTML added to be wrapped in parent div? Have to send a single
      element
    </h1>
  </div>
);

{
  /* need to render stuff in*/
}
ReactDOM.render(what_to_render, document.getElementById("id-goes-here"));

{
  /*stateless functional component recieve and render data but not manage or track changes to it, function that accepts props and return JSX*/
}
const MyComponent = function () {
  return <div className="customClass"> </div>;
};

{
  /*stateless component extends React.Component, but doesn't use internal state */
}
class MyComponent2 extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <h1>Hi!</h1>
      </div>
    );
  }
}

{
  /*can also declare default props*/
}
MyComponent2.defaultProps = {
  location: "San Francisco",
};

{
  /*If you know the prop type you can set it to only receive that */
}
MyComponent.propTypes = { location: PropTypes.string.isRequired };

{
  /*stateful components/React components/components maintain their own internal state, better to minimize using these */
}
class StatefulComponent extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      firstName: "Amir",
    };
  }
  render() {
    return (
      <div>
        <h1>{this.state.firstName}</h1>
      </div>
    );
  }
}
{
  /*passing props to es6 class components */
}
class App extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <Welcome name="chicken shit" />
      </div>
    );
  }
}

class Welcome extends React.Component {
  constructor(props) {
    super(props);
  }
  render() {
    return (
      <div>
        <p>
          Hello, <strong>{this.props.name}</strong>!
        </p>
      </div>
    );
  }
}

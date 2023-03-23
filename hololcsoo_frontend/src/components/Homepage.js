import React, { useState } from 'react';
import { makeStyles } from '@mui/styles';
import TextField from '@mui/material/TextField';

const useStyles = makeStyles(() => ({
  root: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
    height: '100vh',
  },
  form: {
    display: 'flex',
    justifyContent: 'center',
    alignItems: 'center',
  },
  input: {
    borderRadius: 25,
    '&:hover': {
      boxShadow: '0px 0px 0px 2px red',
    },
  },
}));

export default function SearchBar(props) {
  const classes = useStyles();
  const [searchTerm, setSearchTerm] = useState('');

  const handleChange = (event) => {
    setSearchTerm(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // Handle form submission with search term
  };

  return (
    <div className={classes.root}>
      <form className={classes.form} noValidate autoComplete="off" onSubmit={handleSubmit}>
        <TextField
          className={classes.input}
          id="outlined-basic"
          label="Search"
          variant="outlined"
          InputProps={{
            style: { borderRadius: 25 },
          }}
          value={searchTerm}
          onChange={handleChange}
          {...props}
        />
      </form>
    </div>
  );
}
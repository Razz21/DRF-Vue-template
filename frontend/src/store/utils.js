export const tokenConfig = state => {
  const config = {
    headers: {
      "Content-Type": "application/json"
    }
  };
  if (state.token) {
    config.headers["Authorization"] = `Token ${state.token}`;
  }
  return config;
};

export const prepareAlertType = status => {
  // check status code type
  switch ((''+status)[0]) {
    case 1:
    case 3:
      return "info";
    case 2:
      return "success";
    default:
      return "error";
  }
};

function Profile() {
  const user = JSON.parse(localStorage.getItem("user"));

  return (
    <div>
      <h2>Profile Page</h2>
      {user ? (
        <>
          <p>Username: {user.username}</p>
          <p>Email: {user.email}</p>
        </>
      ) : (
        <p>No user data available</p>
      )}
    </div>
  );
}

export default Profile;

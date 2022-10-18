export interface ProfileProps {
  name: string
  age: number
  isSmart?: boolean
}
export default function Profile (props: ProfileProps) {
  const { name, age, isSmart=false } = props;
  return (
  <p>
    {name} - {age} - {isSmart ? "150IQ" : "50IQ"}
  </p>);
}
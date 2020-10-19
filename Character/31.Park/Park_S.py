import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "40 + 1n Wraith", 64, 64);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 2)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 64, 0);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 32, 32);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }
         if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Wraith", 32, 0);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 8)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
      

         f.SkillEnd(cp);
      }
   }
}
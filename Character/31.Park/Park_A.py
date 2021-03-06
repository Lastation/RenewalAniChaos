import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 0);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 100);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);     
         }
         if (f.loop[cp] == 2)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 0);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 50);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 0);
            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 100);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, f.location[cp]);     
         }
         if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 0);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 50, 50);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         if (f.loop[cp] < 7)
         {
            f.SquareShape(cp, 1, "Protoss Dark Archon", -100, 100 - 50 * f.loop[cp]);                     
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere"); 
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
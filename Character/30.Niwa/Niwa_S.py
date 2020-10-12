import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "Bengalaas (Jungle)", 50, 0);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Guardian", 50, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 2)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.SquareShape(cp, 1, "Bengalaas (Jungle)", 50, 50);
            KillUnitAt(All, "Bengalaas (Jungle)", "Anywhere", cp);

            f.SquareShape(cp, 1, "Kakaru (Twilight)", 100, 100);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 50);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.DotShape(cp, 1, "Target", 0, 0);
            KillUnitAt(All, "Target", "Anywhere", cp);


            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 50, 50);
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 100);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.DotShape(cp, 1, "Target", 0, 0);
            KillUnitAt(All, "Target", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Mutalisk", 50, 50);
            KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", cp);

            f.SquareShape(cp, 1, "50 + 1n Battlecruiser", 100, 0);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 0);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, f.location[cp]);
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
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}
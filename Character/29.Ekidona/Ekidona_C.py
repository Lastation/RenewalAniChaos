import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(cp, 1, "60 + 1n Danimoth", 50, 50);
            f.SquareShape(cp, 1, "60 + 1n Archon", 50, 50);
            f.SquareShape(cp, 1, "60 + 1n Danimoth", 100, 100);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 100);            
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);
         }
         else if (f.loop[cp] == 4)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

            f.SquareShape(cp, 1, "60 + 1n Danimoth", 50, 0);
            f.SquareShape(cp, 1, "60 + 1n Archon", 50, 0);
            f.SquareShape(cp, 1, "60 + 1n Danimoth", 100, 0);
            f.SquareShape(cp, 1, "60 + 1n Archon", 100, 0);            
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);

         }
         else if (f.loop[cp] == 8)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);
         }


         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 12)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {
            f.DotShape(cp, 1, "40 + 1n Mojo", 0, 0);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 0);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 50, 50);
            f.SquareShape(cp, 1, "40 + 1n Mojo", 100, 0);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 50, 50);
            f.SquareShape(cp, 1, "60 + 1n High Templar", 100, 0);
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveUnit(All, "60 + 1n High Templar", cp, "[Skill]Unit_Wait_ALL", f.location[cp]);
            Order("60 + 1n High Templar", cp, "Anywhere", Attack, f.location[cp]);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 4)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}
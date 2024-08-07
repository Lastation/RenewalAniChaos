import Function as f;

function main(cp)
{
   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            SetSwitch("ComputerAlliy", Set);
            SetAllianceStatus(P7, Ally);
            SetAllianceStatus(P8, Ally);
            SetDeaths(cp, SetTo, 20, " `ShieldRecharge");
            f.NxNSquareShape(cp, 1, "130 + 1n Norad", 7, 75);
            f.NxNSquareShape(cp, 1, "80 + 1n Goliath", 7, 50);
            Order("130 + 1n Norad", cp, "Anywhere", Attack, f.location[cp]); 
            Order("80 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]); 
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "130 + 1n Norad", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Goliath", "Anywhere", cp);
            f.NxNSquareShape(cp, 1, "130 + 1n Norad", 7, 75);
            f.NxNSquareShape(cp, 1, "80 + 1n Goliath", 7, 50);
            Order("130 + 1n Norad", cp, "Anywhere", Attack, f.location[cp]); 
            Order("80 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]); 
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "130 + 1n Norad", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Goliath", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
         }
         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 10)
         {
         f.count[cp] += 1;
         f.loop[cp] = 0;
         }

      }
         
      if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {
            var x = 50 * f.loop[cp];
            var y = 200 - 50 * f.loop[cp];

            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWaitB(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 8)
         {
            var x = 200 - 50 * (f.loop[cp] - 4);
            var y = -50 * (f.loop[cp] - 4);

            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", y, -x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 11)
         {
            var x = 200 - 50 * (f.loop[cp] - 8);
            var y = -50 * (f.loop[cp] - 8);

            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", y, -x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 11)
         {
            var x = 200 - 50 * (f.loop[cp] - 8);
            var y = -50 * (f.loop[cp] - 8);

            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", y, -x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loop[cp] += 1;
         }
                  if (f.loop[cp] == 12)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }

      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] < 4)
         {
            var x = 50 * f.loop[cp];
            var y = 200 - 50 * f.loop[cp];

            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", y, -x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 8)
         {
            var x = 200 - 50 * (f.loop[cp] - 4);
            var y = -50 * (f.loop[cp] - 4);

            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", y, -x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] < 11)
         {
            var x = 200 - 50 * (f.loop[cp] - 8);
            var y = -50 * (f.loop[cp] - 8);

            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", y, -x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 11)
         {
            var x = 200 - 50 * (f.loop[cp] - 8);
            var y = -50 * (f.loop[cp] - 8);

            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", x, y);
            f.DotShape(cp, 1, "50 + 1n Tank", x, y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -x, -y);
            f.DotShape(cp, 1, "50 + 1n Tank", -x, -y);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", -y, x);
            f.DotShape(cp, 1, "Protoss Dark Archon", -y, x);
            f.DotShape(cp, 1, "80 + 1n Tom Kazansky", y, -x);
            f.DotShape(cp, 1, "Protoss Dark Archon", y, -x);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("80 + 1n Tom Kazansky", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWaitB(cp, 80);

            f.loop[cp] += 1;
         }
         if (f.loop[cp] == 12)
         {
            RemoveUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "40 + 1n Goliath", "Anywhere", cp);
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 3)
      {
         if (f.loop[cp] < 6)
         {
            f.NxNSquareShape(cp, 1, "130 + 1n Norad", 1 + f.loop[cp], 125);
            f.NxNSquareShape(cp, 1, "80 + 1n Goliath", 1 + f.loop[cp], 125);     
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("130 + 1n Norad", cp, "Anywhere", Attack, f.location[cp]);     
            Order("80 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);    
         }

       f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "130 + 1n Norad", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Goliath", "Anywhere", cp);
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 4)
      {
         if (f.loop[cp] < 6)
         {
            f.NxNSquareShape(cp, 1, "130 + 1n Norad", 7 - f.loop[cp], 125);
            f.NxNSquareShape(cp, 1, "80 + 1n Goliath", 7 - f.loop[cp], 125); 
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("130 + 1n Norad", cp, "Anywhere", Attack, f.location[cp]);     
            Order("80 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);     
         }

       f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "130 + 1n Norad", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Goliath", "Anywhere", cp);
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 5)
      {
         if (f.loop[cp] < 6)
         {
            f.NxNSquareShape(cp, 1, "130 + 1n Norad", 1 + f.loop[cp], 125);
            f.NxNSquareShape(cp, 1, "80 + 1n Goliath", 1 + f.loop[cp], 125);     
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("130 + 1n Norad", cp, "Anywhere", Attack, f.location[cp]);     
            Order("80 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);      
         }

       f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 6)
         {
            KillUnitAt(All, "130 + 1n Norad", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Goliath", "Anywhere", cp);
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 6)
      {

         if (f.loop[cp] < 6)
         {
            f.NxNSquareShape(cp, 1, "130 + 1n Norad", 7 - f.loop[cp], 125);
            f.NxNSquareShape(cp, 1, "80 + 1n Goliath", 7 - f.loop[cp], 125);       
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("130 + 1n Norad", cp, "Anywhere", Attack, f.location[cp]);     
            Order("80 + 1n Goliath", cp, "Anywhere", Attack, f.location[cp]);    
         }

       f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 6)
         {
            SetSwitch("ComputerAlliy", Clear);
            if (cp < 3)
            {
               SetAllianceStatus(P8, Enemy);
            }
            else
            {
               SetAllianceStatus(P7, Enemy);
            }
            KillUnitAt(All, "130 + 1n Norad", "Anywhere", cp);
            KillUnitAt(All, "80 + 1n Goliath", "Anywhere", cp);
            SetDeaths(cp, SetTo, 0, " `ShieldRecharge");

            f.SkillEnd(cp);        
            f.count[cp] += 1;
            f.loop[cp] = 0; 

         }
      }
   }
}
